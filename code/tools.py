import json

class tools () :

    def get_currencies():
        # Ouvrir le fichier "currencies.json".
        f = open('currencies.json', 'r')
        # mettre le contenu du fichier dans "currencies".
        currencies = json.loads(f.read())['currencies']
        # Fermer le fichier
        f.close()
        return currencies

    def get_list_of_keys(self, key):
        currencies = self.get_currencies()
        # Récupérer les valeurs une par une.
        return [item[key] for item in currencies]

    def get_symbol_from_name(self, name):
        for item in self.get_currencies():
            if item['id'] == name:
                # Retourner le trigrame pour chaque monaie.
                return item['symbol']

    def get_keys():
        # Futur fonction  pour redécouper
        pass

    def get_keys_and_join_from_currencies_file(self, key, join_separator, add_hashtag=False):
        currencies = self.get_currencies()

        if add_hashtag:
            # Ajouter un hashtag devant
            return join_separator.join(['#{}'.format(item[key]) for item in currencies])
        # Ne pas mettre de hashtag
        return join_separator.join([item[key] for item in currencies])