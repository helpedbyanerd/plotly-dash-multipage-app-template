from dash import ctx

def get_trigger() -> str:
    return ctx.triggered[0]["prop_id"]