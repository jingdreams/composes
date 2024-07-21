# Dockerfile - Ubuntu Jammy
# https://github.com/openresty/docker-openresty

FROM openresty/openresty:jammy

# LABEL maintainer="Li'on <lion@goldpomelo.com>"

# Docker Build Arguments
ARG DIR="/usr/local/openresty"

RUN mkdir ${DIR}/geoipupdate
COPY GeoLite2-City.mmdb ${DIR}/geoipupdate
COPY GeoLite2-Country.mmdb ${DIR}/geoipupdate
COPY GeoIP.conf ${DIR}/geoipupdate
COPY geoipupdate ${DIR}/geoipupdate
COPY getlocation.conf /etc/nginx/conf.d

RUN luarocks install lua-resty-maxminddb \
    && rm -f /etc/nginx/conf.d/default.conf \
    && sh -c "echo /usr/local/lib  >> /etc/ld.so.conf.d/local.conf" \
    && ldconfig