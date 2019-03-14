from UnleashClient.utils import LOGGER

# pylint: disable=dangerous-default-value, broad-except
class Variant:
    def __init__(self,
                 name: str,
                 weight: int,
                 payload: dict,
                 overrides: list) -> None:
                 # enabled: bool) -> None:
        """
        An representation of a variation object

        :param name: Name of the variation.
        :param enabled: Whether variation is enabled.
        :param strategies: List of sub-classed Strategy objects representing feature strategies.
        """
        # Experiment information
        self.name = name
        # self.enabled = enabled
        self.weight = weight
        self.payload = payload
        self.overrides = overrides

    def overrides_matches_contest(context: dict) -> bool:
      for o in overrides:
        if o.matches_context?(context)
          return True
      return False
