CAESAR
===

Experimenting around with data and maps with the vague idea of making a tool for running D&D Hexcrawl-type adventures on a reality-based map.

![CAESAR Screenshot](/docs/images/Screenshot 2023-11-29 at 11-28-30 CAESAR.png?raw=true)

At present, this displays a hex grid (H3Geo, resolution 6) over the state of Arkansas. Each hex has a fill color based on the 2023 Cropland Data Layer from the USDA. The outline of each hex is colored based on elevation data. The elevation data is from the USGS DEM. The outline color is based on the elevation change within the hex. Mostly this is on a yellow-to-dark-red color map. Where the maximum elevation is over 600m, and the elevation change is more than 300m--this is roughly the old definition for a "mountain"--the outline color is grey.

---

To run:

- Use the `Containerfile` with `podman`, or
- Install the package in your Python environment and then execute `caesar`

---

