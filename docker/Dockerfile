# spécification de l'image de base à utiliser pour la première étape de la construction de l'image.
FROM node:16-alpine AS node
# Utiliser l'image officielle de grafana OSS.
FROM grafana/grafana-oss

# Spécification de l'utilisateur à utiliser pour les commandes suivantes.
USER root
# Copie des fichiers de l'image node à l'image en construction. 
COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/share /usr/local/share
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin

# Ajout du fichier du répertoire courrant vers l'image en construction.
ADD ./custom-run.sh /custom-run.sh
# Permet de lancer le commandes suivantes comme les mise à jour, clone git etc.
RUN apk update \
    && apk upgrade \
    && apk add --no-cache git \
    && git clone https://github.com/JamesOsgood/mongodb-grafana $GF_PATHS_PLUGINS/mongodb-grafana \
    && sed -i 's/grafana-mongodb-datasource/jamesosgood-grafana-mongodb-datasource/g' $GF_PATHS_PLUGINS/mongodb-grafana/dist/plugin.json \
    && rm -rf $GF_PATHS_PLUGINS/mongodb-grafana/.git \
    && npm install --silent --prefix $GF_PATHS_PLUGINS/mongodb-grafana \
    && npm cache clean --force --prefix $GF_PATHS_PLUGINS/mongodb-grafana \
    && apk del --no-cache git \
    && chmod +x /custom-run.sh \
    && sed -i 's/;allow_loading_unsigned_plugins =.*/allow_loading_unsigned_plugins = jamesosgood-grafana-mongodb-datasource/g' $GF_PATHS_CONFIG
# Lancement de costum-run.sh
ENTRYPOINT ["/custom-run.sh"]