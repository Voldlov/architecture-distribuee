from MongoDBConnecteur import MongoDBConnecteur

mongo_connector = MongoDBConnecteur("<username>", "<password>", "<cluster>", "<db_name>")
data = mongo_connector.get_data("collection_name")