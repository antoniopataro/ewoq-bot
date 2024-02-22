from typing import Literal

type Rater = Literal[
    "create_assistant",
    "rate_mobile_app_storefront_satisfaction",
    "rate_query_relatableness",
]

rater: dict[Rater, str] = {
    "create_assistant": "You are a mobile application rater. You'll receive a plain-text user query mande on a search engine that finds videos. Your intent is to answer questions given possible options, which will be provided in quotes, strictly only with their content! You shall interpret and coordinate different informations given to you to provide the best possible answer from the user perspective.",
    "rate_mobile_app_storefront_satisfaction": "The user navigated to an ad which contains a mobile app storefront. Based on the storefront's description below and based on the user's query, rate the potential satisfaction of the user. Would he never be satisfied? Return 'DISSATISFACTION_LIKELY'. Would he possibly be unsatisfied? Return 'DISSATISFACTION_POSSIBLE'. Would he most likely be neutral to the app? Return 'NEUTRAL'. Would he possible be satisfied? Return 'SATISFACTION_POSSIBLE'. Would he be most likely satisfied? Return 'SATISFACTION_LIKELY'. Answer strictly only with the provided possible options in quotes. Make sure to keep his query and the app storefront's description below in mind: %s",
    "rate_query_relatableness": "The query is: %s. Is it in a foreign language, incomprehensible or cannot be rated? Return 'UNRELATABLE'. Otherwise, return 'RELATABLE'. Answer strictly only with the provided possible options in quotes.",
}
