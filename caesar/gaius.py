import dash_bootstrap_components as dbc
from dash import html, page_container, page_registry

from caesar.app import app

navbar = html.Div(
    [
        dbc.NavbarSimple(
            [
                dbc.NavItem(
                    dbc.NavLink(
                        page["title"],
                        href=page["path"],
                    )
                )
                for page in page_registry.values()
                if page["path"] != "/"
            ],
            brand=page_registry["pages.index"]["title"],
            brand_href=page_registry["pages.index"]["path"],
        ),
    ],
)

app.layout = html.Div([navbar, page_container])

julius = app.server


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
