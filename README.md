# My Content : Books recommandation mobile app

This repository is part of a 3-repos project :

- Main repo : [My Content : Books recommandation mobile app](https://github.com/fleuryc/OC_AI-Engineer_P9_Books-recommandation-mobile-app)
- [Azure Function](https://github.com/fleuryc/oc_p9_function "Azure Function") : **this repo**
- [Mobile App](https://github.com/fleuryc/oc_p9_mobile-app "Mobile App")

## Goals

Create an [Azure Function](https://azure.microsoft.com/en-us/services/functions/ "Azure Functions") that will return a list of relevant articles stored in [Azure CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/ "Azure CosmosDB")

## Installation

### Prerequisites

- [Python 3.9](https://www.python.org/downloads/ "Python 3.9")

### Dependencies

```bash
# pip install azure-functions
# > or just :
pip install -r requirements.txt
```

### Azure resources

The app will query a [Azure CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/ "Azure CosmosDB") database to retrieve a list of relevant articles.

- [Azure Cosmos DB input binding for Azure Functions 2.x and higher - HTTP trigger, look up ID from route data](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?tabs=in-process%2Cfunctionsv2&pivots=programming-language-python#http-trigger-look-up-id-from-route-data-python "Azure Cosmos DB input binding for Azure Functions 2.x and higher - HTTP trigger, look up ID from route data")

### Environment variables

- Set environment variable values in [local.settings.json](local.settings.json) file (copy or rename [local.settings.example.json](local.settings.example.json)).
