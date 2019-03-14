from UnleashClient.utils import LOGGER


# pylint: disable=dangerous-default-value, broad-except
class Feature:
    def __init__(self,
                 name: str,
                 enabled: bool,
                 strategies: list
                 variant_definitions: list) -> None:
        """
        An representation of a fewature object

        :param name: Name of the feature.
        :param enabled: Whether feature is enabled.
        :param strategies: List of sub-classed Strategy objects representing feature strategies.
        """
        # Experiment information
        self.name = name
        self.enabled = enabled
        self.strategies = strategies
        self.variant_definitions = variant_definitions

        # Stats tracking
        self.yes_count = 0
        self.no_count = 0

    def reset_stats(self) -> None:
        """
        Resets stats after metrics reporting

        :return:
        """
        self.yes_count = 0
        self.no_count = 0

    def increment_stats(self, result: bool) -> None:
        """
        Increments stats.

        :param result:
        :return:
        """
        if result:
            self.yes_count += 1
        else:
            self.no_count += 1

    def is_enabled(self,
                   context: dict = None,
                   default_value: bool = False) -> bool:
        """
        Checks if feature is enabled.

        :param context: Context information
        :param default_value: Optional, but allows for override.
        :return:
        """
        flag_value = default_value

        if self.enabled:
            try:
                for strategy in self.strategies:
                    flag_value = flag_value or strategy(context)
            except Exception as strategy_except:
                LOGGER.warning("Error checking feature flag: %s", strategy_except)

        self.increment_stats(flag_value)

        LOGGER.info("Feature toggle status for feature %s: %s", self.name, flag_value)

        return flag_value

    def get_variant(self,
                    context: dict = None,
                    fallback_variant: Variant = None) -> Variant:
        """
        """
              # fallback_variant = disabled_variant if fallback_variant.nil?
        if not is_enabled(context):
            return disabled_variant

        variant = get_variant_from_override_match(context)
        variant = get_variant_from_weights(context) if variant.nil?

        return None

    def get_variant_from_override_match(self,
                                        context: dict = None) -> Variant:
        """
            If an override matches, return the variant.
        """
        return None
