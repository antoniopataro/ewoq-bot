from typing import Literal


type Rater = Literal[
    "create_assistant",
    "interpret_query",
    "rate_ad_creative_usefulness",
]

rater: dict[Rater, str] = {
    "create_assistant": "You are a web advertisement rater. You'll receive a plain-text user query made on a search engine, potentially followed by an ad and/or a landing page. Your intent is to answer questions given possible options, which will be provided in quotes, strictly only with their content! You shall interpret and coordinate different informations given to you to provide the best possible answer from the user perspective.",
    "interpret_query": "The query is: %s. Is it missing? Return 'MISSING'. Is it not in english? Return 'NON_ENGLISH'. Does it contain unexpected porn? Return 'UNEXPECTED_PORN'. Do you understand the query or its possible intent? Return 'YES'. Otherwise, return 'NO'. Answer strictly only with the provided possible options in quotes.",
    "rate_ad_creative_usefulness": "The ad creative text is: %s. Did it not load? Return 'ERROR/DID_NOT_LOAD'. Is it in the wrong language? Return 'WRONG_LANGUAGE'. Does it contain unexpected porn? Return 'UNEXPECTED_PORN'. Could it be useful? Return 'COULD_BE_USEFUL'. Otherwise, return 'COULD_NEVER_BE_USEFUL'. Keep the given query in mind, if it diverges, be strict. If links or prices are provided, ignore them. Answer strictly only with the provided possible options in quotes.",
}

type RawRightPrompt = Literal[
    "After researching the query, do you understand what the\nuser wants?",
    "Before interacting with the ad, is it already clear that the ad\ncould never be useful for this query?",
    "After interacting with the ad (e.g. visiting the landing page),\ndo any of these descriptions apply?",
    "Does the ad creative accurately represent the landing\npage?",
    "Does the ad match a reasonable interpretation of the\nquery?",
    "How closely does the ad address the user's intent?",
    "By interacting with this ad, does the user make clear\nprogress towards the goal offered by the ad?",
    "How well does the ad satisfy requirements in the query (e.g.\nlocation, brands, product features)?",
    "Does the ad offer an alternative to what the user seeks?",
    "Review your responses",
    "Does the ad seem useful for the given query?",
]

raw_right_prompts: list[RawRightPrompt] = [
    "After researching the query, do you understand what the\nuser wants?",
    "Before interacting with the ad, is it already clear that the ad\ncould never be useful for this query?",
    "After interacting with the ad (e.g. visiting the landing page),\ndo any of these descriptions apply?",
    "Does the ad creative accurately represent the landing\npage?",
    "Does the ad match a reasonable interpretation of the\nquery?",
    "How closely does the ad address the user's intent?",
    "By interacting with this ad, does the user make clear\nprogress towards the goal offered by the ad?",
    "How well does the ad satisfy requirements in the query (e.g.\nlocation, brands, product features)?",
    "Does the ad offer an alternative to what the user seeks?",
    "Review your responses",
    "Does the ad seem useful for the given query?",
]

type RightPrompt = Literal[
    "After researching the query, do you understand what the user wants?",
    "Before interacting with the ad, is it already clear that the ad could never be useful for this query?",
    "After interacting with the ad (e.g. visiting the landing page), do any of these descriptions apply?",
    "Does the ad creative accurately represent the landing page?",
    "Does the ad match a reasonable interpretation of the query?",
    "How closely does the ad address the user's intent?",
    "By interacting with this ad, does the user make clear progress towards the goal offered by the ad?",
    "How well does the ad satisfy requirements in the query (e.g. location, brands, product features)?",
    "Does the ad offer an alternative to what the user seeks?",
    "Review your responses",
    "Does the ad seem useful for the given query?",
]

right_prompts: list[RightPrompt] = [
    "After researching the query, do you understand what the user wants?",
    "Before interacting with the ad, is it already clear that the ad could never be useful for this query?",
    "After interacting with the ad (e.g. visiting the landing page), do any of these descriptions apply?",
    "Does the ad creative accurately represent the landing page?",
    "Does the ad match a reasonable interpretation of the query?",
    "How closely does the ad address the user's intent?",
    "By interacting with this ad, does the user make clear progress towards the goal offered by the ad?",
    "How well does the ad satisfy requirements in the query (e.g. location, brands, product features)?",
    "Does the ad offer an alternative to what the user seeks?",
    "Review your responses",
    "Does the ad seem useful for the given query?",
]
