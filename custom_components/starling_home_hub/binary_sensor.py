"""Binary sensor platform for starling_home_hub."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)

from .const import DOMAIN
from .coordinator import StarlingHomeHubDataUpdateCoordinator
from .entity import StarlingHomeHubEntity

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="starling_home_hub",
        name="Integration Blueprint Binary Sensor",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        StarlingHomeHubBinarySensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class StarlingHomeHubBinarySensor(StarlingHomeHubEntity, BinarySensorEntity):
    """starling_home_hub binary_sensor class."""

    def __init__(
        self,
        coordinator: StarlingHomeHubDataUpdateCoordinator,
        entity_description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def is_on(self) -> bool:
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
