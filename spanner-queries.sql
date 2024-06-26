SELECT
  fund_name
FROM
  EU_MutualFunds
WHERE
  SEARCH(fund_name_Tokens,
    'MSCI Japan');
SELECT
  fund_name
FROM
  EU_MutualFunds
WHERE
  fund_name LIKE "%MSCI%Japan%";
SELECT
  fund_name
FROM
  EU_MutualFunds
WHERE
  SEARCH(fund_name_Tokens,
    'MSCI Japan')
  AND fund_name NOT IN (
  SELECT
    fund_name
  FROM
    EU_MutualFunds
  WHERE
    fund_name LIKE "%MSCI%Japan%" );



SELECT DISTINCT fund_name,
    investment_strategy
FROM EU_MutualFunds
WHERE SEARCH(
        investment_strategy_Tokens,
        'derivatives dividend europe OR asia'
    )
order by fund_name;


SELECT
 DISTINCT fund_name,investment_strategy
FROM
  EU_MutualFunds
WHERE
  investment_strategy LIKE "%derivatives%Europe%" ;



SELECT
  DISTINCT fund_name,investment_strategy
FROM
  EU_MutualFunds
WHERE
  SEARCH(investment_strategy_Tokens,
    'derivatives europe') order by fund_name;

  

SELECT
  DISTINCT fund_name,investment_strategy
FROM
  EU_MutualFunds
WHERE
  SEARCH(investment_strategy_Tokens,
    'commodity ETF') order by fund_name;


SELECT DISTINCT fund_name,
    investment_managers
FROM EU_MutualFunds
WHERE SEARCH(investment_managers_Tokens, 'Whitmore OR Billy')
order by fund_name;
SELECT DISTINCT fund_name,
    investment_strategy
FROM EU_MutualFunds
WHERE SEARCH(investment_strategy_Tokens, 'derivatives europe')
order by fund_name;
SELECT fund_name
FROM EU_MutualFunds
WHERE SEARCH(fund_name_Tokens, 'MSCI Japan');
SELECT fund_name
FROM EU_MutualFunds
WHERE fund_name LIKE "%MSCI%Japan%";
SELECT fund_name
FROM EU_MutualFunds
WHERE SEARCH(fund_name_Tokens, 'MSCI Japan')
    AND fund_name NOT IN (
        SELECT fund_name
        FROM EU_MutualFunds
        WHERE fund_name LIKE "%MSCI%Japan%"
    );

SELECT DISTINCT fund_name,
    investment_strategy
FROM EU_MutualFunds
WHERE SEARCH(
        investment_strategy_Tokens,
        'derivatives dividend europe OR asia'
    )
order by fund_name;
SELECT DISTINCT fund_name,
    investment_strategy
FROM EU_MutualFunds
WHERE investment_strategy LIKE "%derivatives%Europe%";
SELECT DISTINCT fund_name,
    investment_strategy
FROM EU_MutualFunds
WHERE SEARCH(investment_strategy_Tokens, 'derivatives europe')
order by fund_name;
SELECT DISTINCT fund_name,
    investment_strategy
FROM EU_MutualFunds
WHERE SEARCH(investment_strategy_Tokens, 'commodity ETF')
order by fund_name;
select DISTINCT investment_managers
from EU_MutualFunds
WHERE SEARCH(investment_managers_Tokens, 'Briand');
select investment_strategy
from EU_MutualFunds
WHERE SEARCH(
        investment_strategy_Tokens,
        '51 AROUND(10) Equity -Russia Norway'
    )
ORDER BY SCORE (
        investment_strategy_Tokens,
        '51 AROUND(10) Equity -Russia Norway'
    );
SELECT DISTINCT fund_name,
    investment_managers,
    investment_strategy
FROM EU_MutualFunds
WHERE SEARCH(
        TOKENLIST_CONCAT(
            [investment_managers_Tokens,investment_strategy_Tokens]
        ),
        'Whitmore OR Billy derivatives europe'
    )
order by fund_name;
SELECT DISTINCT fund_name,
    investment_managers,
    investment_managers
FROM EU_MutualFunds
WHERE SEARCH(
        TOKENLIST_CONCAT(
            [investment_managers_Tokens,investment_strategy_Tokens]
        ),
        'Whitmore OR Billy derivatives europe'
    )
order by fund_name;
-- SELECT fund_name, investment_managers, investment_managers, COSINE_DISTANCE(
-- investment_strategy_Embedding ,
-- (   SELECT embeddings.values
-- FROM ML.PREDICT(
-- MODEL EmbeddingsModel,
-- (SELECT "I'd like to invest in environment friendly funds" as content)
-- )
-- )
-- ) as distance
-- FROM EU_MutualFunds
-- ORDER BY distance
-- LIMIT 5;


SELECT fund_name,
    investment_strategy,
    COSINE_DISTANCE(
        investment_strategy_Embedding,
        (
            SELECT embeddings.
            VALUES
            FROM ML.PREDICT(
                    MODEL EmbeddingsModel,
                    (
                        SELECT "Invest in US based companies that align with investment criteria regarding environmental and social impact" AS content
                    )
                )
        )
    ) AS distance
FROM EU_MutualFunds
WHERE investment_strategy_Embedding is not NULL
ORDER BY distance
LIMIT 10;
select distinct fund_name,
                investment_managers,
                investment_strategy
  from eu_mutualfunds
 where search(
	tokenlist_concat(
		[
			investment_managers_tokens,
			investment_strategy_tokens
		]
	),
	'Edward OR Elizabeth derivatives europe'
)
 order by fund_name;

select investment_managers
  from eu_mutualfunds
 where search_substring(
	investment_managers_substring_tokens,
	'Ed Dom'
);

SELECT fund_name, investment_strategy,investment_managers, COSINE_DISTANCE( investment_strategy_Embedding, (SELECT embeddings. VALUES FROM ML.PREDICT( MODEL EmbeddingsModel, (SELECT 'Invest in companies which also subscribe to my ideas around climate change, doing good for the planet' AS content) ) ) ) AS distance FROM EU_MutualFunds WHERE investment_strategy_Embedding is not NULL AND search_substring(investment_managers_substring_tokens, 'Brian') ORDER BY distance LIMIT 10;
SELECT fund_name, investment_strategy,investment_managers, COSINE_DISTANCE( investment_strategy_Embedding, (SELECT embeddings. VALUES FROM ML.PREDICT( MODEL EmbeddingsModel, (SELECT 'Invest in companies which also subscribe to my ideas around climate change, doing good for the planet' AS content) ) ) ) AS distance FROM EU_MutualFunds WHERE investment_strategy_Embedding is not NULL ORDER BY distance LIMIT 10;


select distinct investment_strategy
  from eu_mutualfunds
 where search(
	investment_strategy_tokens,
	'Technology'
);


GRAPH FundGraph
MATCH (fund:Fund {NewMFSequence:750693762887319552})<-[:Manages]-(manager:Manager)
RETURN fund.fund_name as fund_name, manager.name as manager_name
