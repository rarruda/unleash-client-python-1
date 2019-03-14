

class VariantDefinition:
    def __init__(self,
                 name: str,
                 weight: int = 0,
                 payload: dict = None,
                 overrides: list = None):
        self.name = name
        self.weight = weight
        self.payload = payload
        self.overrides = overrides

    def override_matches_context(self, context) -> bool:
      return None