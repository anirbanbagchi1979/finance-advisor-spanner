from google.cloud import spanner
from google.cloud import spanner
import pandas as pd

# Your Cloud Spanner instance ID.
instance_id = "spanner-fts"
# Your Cloud Spanner database ID.
database_id = "mf-data"
# Instantiate a client.
spanner_client = spanner.Client()

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)
# Get a Cloud Spanner database by ID.
database = instance.database(database_id)


def spanner_read_data(query):
    # Execute a simple SQL statement.
    outputs = []
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(query)
        rows = list()
        for row in results:
            rows.append(row)
        # Get column names
        cols = [x.name for x in results.fields]
        # Convert to pandas dataframe
        result_df = pd.DataFrame(rows, columns=cols)
    return result_df


def fts_query(query_params):
    print("Query Part", query_params)

    if query_params[1] == "":
        query = (
            "SELECT DISTINCT fund_name,investment_strategy,investment_managers,fund_trailing_return_ytd,top5_holdings FROM EU_MutualFunds WHERE SEARCH(investment_strategy_Tokens, '"
            + query_params[0]
            + "') order by fund_name;"
        )
    else:
        query = (
            "SELECT DISTINCT fund_name, investment_managers, investment_strategy FROM EU_MutualFunds WHERE SEARCH_SUBSTRING(investment_managers_Substring_Tokens, '"
            + query_params[1]
            + "') AND SEARCH(investment_strategy_Tokens, '"
            + query_params[0]
            + "') ORDER BY fund_name;"
        )
    returnVals = dict()
    returnVals["query"] = query
    print("FTS Query", query)
    df = spanner_read_data(query)

    returnVals["data"] = df
    return returnVals


def semantic_query(query_params):
    print("Query Part", query_params)

    query = (
        "SELECT fund_name, investment_strategy,investment_managers, COSINE_DISTANCE( investment_strategy_Embedding, (SELECT embeddings. VALUES FROM ML.PREDICT( MODEL EmbeddingsModel, (SELECT '"
        + query_params[0]
        + "' AS content) ) ) ) AS distance FROM EU_MutualFunds WHERE investment_strategy_Embedding is not NULL  AND  search_substring(investment_managers_substring_tokens, '"
        + query_params[1]
        + "')ORDER BY distance LIMIT 10;"
    )

    returnVals = dict()
    returnVals["query"] = query
    print("Semantic Query", query)
    df = spanner_read_data(query)

    returnVals["data"] = df
    return returnVals


def like_query(query_params):
    if query_params[1] == "EXCLUDE":
        query_params[1] = "AND"
    query = (
        " SELECT DISTINCT fund_name, investment_managers, investment_strategy FROM EU_MutualFunds WHERE investment_managers LIKE ('%"
        + query_params[3]
        + "%') AND ( investment_strategy LIKE ('%"
        + query_params[0]
        + "%') "
        + query_params[1]
        + " investment_strategy LIKE ('%"
        + query_params[2]
        + "%') ) ORDER BY fund_name;"
    )
    print(query)

    # df = spanner_read_data(query)
    returnVals = dict()
    returnVals["query"] = query
    print("FTS Query", query)
    df = spanner_read_data(query)

    returnVals["data"] = df
    return returnVals


def compliance_query(query_params):
    print("Query Part", query_params)

    query = (
        "GRAPH FundGraph MATCH (sector:Sector {sector_name: '"
        + query_params[0]
        + "'})<-[:BELONGS_TO]-(company:Company)<-[h:HOLDS]-(fund:Fund) RETURN fund.fund_name, SUM(h.percentage) AS totalHoldings GROUP BY fund.fund_name NEXT FILTER totalHoldings > "
        + query_params[1]
        + " RETURN fund_name, totalHoldings"
    )

    returnVals = dict()
    returnVals["query"] = query
    print("Compliance Query", query)
    df = spanner_read_data(query)

    returnVals["data"] = df
    return returnVals
