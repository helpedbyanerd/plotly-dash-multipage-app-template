import dash_mantine_components as dmc


def create_card(image_src: str, title: str, text: str):
    return dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=image_src,
                    height=200,
                )
            ),
            dmc.Group(
                [
                    dmc.Text(children=title, weight=500),
                ],
                position="apart",
                mt="md",
                mb="xs",
            ),
            dmc.Text(
                children=text,
                size="sm",
                color="dimmed",
            ),
            dmc.Group(
                [
                    dmc.Badge("DMC", variant="outline", color="blue"),
                    dmc.Badge("Plotly", variant="outline", color="indigo"),
                    dmc.Badge("Dash", variant="outline", color="lime"),
                ],
                position="apart",
                mt="md",
                mb="xs",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 475, "height": 500},
    )