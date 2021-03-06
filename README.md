# Docker image for JS and HTML injection based on mitmproxy

This repository contains the code for a docker image that runs a proxy which injects javascript and html content into a specific webpage at a specific location. It runs the [mitmproxy](https://mitmproxy.org/) and is based on the
[mitmproxy/mitmproxy image](https://hub.docker.com/r/mitmproxy/mitmproxy/).

## Modifications to the basic image
* contains an addon that injects local scripts and html into a specific webpage
* uses the command-line-version `mitmdump` instead of the interactive `mitmproxy` so it can be run as a service on a cloud platform such as Kubernetes
* has basic authentication configured to restrict access to the proxy
* removes caching headers by setting the [anticache flag](https://docs.mitmproxy.org/stable/overview-features/#anticache)


## Start injecting ...

* Build: `docker build . -t proxy`
* Run: `docker run -p 8080:8080 -t proxy`


## Authentication

Default credentials are set in the Dockerfile. You can configure the credentials by passing the environment variables `USER` and `PASSWORD` when running the image.

Example:
`docker run -p 8080:8080 -e USER=admin -e PASSWORD=password -t proxy`
