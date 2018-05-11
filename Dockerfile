# https://hub.docker.com/r/mitmproxy/mitmproxy/
FROM mitmproxy/mitmproxy:latest

# Add scripts to image
ADD injection_addon.py injection_addon.py
ADD script.js script.js

# Install required packages
RUN pip3 install bs4

# Default credentials
ENV USER user
ENV PASSWORD password

ENTRYPOINT ["/bin/sh",  "-c", "mitmdump --proxyauth ${USER}:${PASSWORD} --anticache -s /injection_addon.py"]
