window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        crop_style: function(feature, context) {
            style = {};
            const value = feature.properties['crop_color']; // get value the determines the color
            style.fillColor = value; // set the fill color according to the class
            return style;
        },
        function1:
    }
});