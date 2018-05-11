from bs4 import BeautifulSoup
from mitmproxy import ctx, http

def read_file(filename):
    with open(filename) as f:
        return f.read()

def response(flow: http.HTTPFlow):
    if flow.request.pretty_host != "example.com":
        return

    if not ("text/html" in flow.response.headers["content-type"]):
        return

    html = BeautifulSoup(flow.response.content, "html.parser")
    if html.body:
        tag = html.body.find("h1")
        if tag:
            ctx.log.info("Inject script and html content ...")

            # create and insert div tag
            div = html.new_tag('div', style="width: inherit;")
            tag.insert_after(div)

            # load and insert local script
            script = html.new_tag("script", type="text/javascript")
            script.insert(0, read_file("/script.js"))
            html.body.append(script)

            # set modified response body
            flow.response.content = str(html).encode("utf8")
