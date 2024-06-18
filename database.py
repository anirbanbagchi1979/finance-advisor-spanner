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
        result_df = pd.DataFrame(rows, columns = cols)
  return result_df

def fts_query(query_params):
    print("Query Part",query_params)

    if(query_params[1]==''):
        query = "SELECT DISTINCT fund_name,investment_strategy,investment_managers,fund_trailing_return_ytd,top5_holdings FROM EU_MutualFunds WHERE SEARCH(investment_strategy_Tokens, '"+query_params[0]+"') order by fund_name;"
    else:
        query = "SELECT DISTINCT fund_name,investment_managers,investment_strategy FROM EU_MutualFunds WHERE SEARCH(investment_managers_Tokens, '"+query_params[1]+"') AND SEARCH(investment_strategy_Tokens, '"+query_params[0]+"') order by fund_name;"
    returnVals = dict(); 
    returnVals['query'] = query
    print("FTS Query",query)
    df = spanner_read_data(query);

    returnVals['data'] = df
    return returnVals

def semantic_query(query_params):
    print("Query Part",query_params)

    query = "SELECT fund_name, investment_strategy,investment_managers, COSINE_DISTANCE( investment_strategy_Embedding, (SELECT embeddings. VALUES FROM ML.PREDICT( MODEL EmbeddingsModel, (SELECT '"+query_params[0]+"' AS content) ) ) ) AS distance FROM EU_MutualFunds WHERE investment_strategy_Embedding is not NULL ORDER BY distance LIMIT 10;"
    
    returnVals = dict(); 
    returnVals['query'] = query
    print("Semantic Query",query)
    df = spanner_read_data(query);

    returnVals['data'] = df
    return returnVals

def like_query(query_part):
  query = "SELECT DISTINCT complaint_id, Consumer_Complaint from Complaints  where Consumer_Complaint LIKE '%" +query_part+"%'  order by complaint_id asc"
  print(query)

  df = spanner_read_data(query);
  print("Printing output")
  print(df)
  return df