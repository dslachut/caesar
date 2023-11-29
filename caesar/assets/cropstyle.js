console.log('loaded!!!')

window.myNamespace = Object.assign(
    {},
    window.myNamespace,
    {  
        mySubNamespace: {  
            crop_style: function (feature, context){
                const {style, colorscale, classes} = context.hideout;
                const value = feature.properties['crop_color'];
                const er = feature.properties['elev_range'];
                const em = feature.properties['elev_max'];
                style.fillColor = value;
                for (let i = 0; i < classes.length; ++i) {
                    if (er > classes[i]) {
                        style.color = colorscale[i];
                    }
                }
                if ((em > 600) && (er > 300)) {
                    style.color = 'grey';
                }
                return style;
            }
        }
    }  
);
