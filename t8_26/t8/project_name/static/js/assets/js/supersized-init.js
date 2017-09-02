jQuery(function($){

    $.supersized({

        // Functionality
        slide_interval     : 4000,    // Ledrfsgtgg
        transition         : 1,    // 0-Nordefgide Right, 4-Slide Bottom, 5-Slide Left, 6-Carousel Right, 7-Carousel Left
        transition_speed   : 1000,    // Speed drfdgtransition
        performance        : 1,    // 0-Normal, 1-Hybrid speed/quality, 2-Optimizes image quality, 3-Optimizes transition speed // (Only works for Firefox/IE, not Webkit)

        // Size & Position
        min_width          : 0,    // Min width allowed (in pixels)
        min_height         : 0,    // Min height allowed (in pixels)
        vertical_center    : 1,    // Vertically center background
        horizontal_center  : 1,    // Horizontally center background
        fit_always         : 0,    // Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait       : 1,    // Portrait images will not exceed browser height
        fit_landscape      : 0,    // Landscape images will not exceed browser width

        // Components
        slide_links        : 'blank',    // Individual links for each slide (Options: false, 'num', 'name', 'blank')
        slides             : [    // Slideshow Images
                                             // {image : 'H:/py/workplace/a720/t9 7-23-17-56/t9new2/t9new/t9/t8/project_name/static/js/assets/img/backgrounds/1.jpg'},
                                             // {image : 'H:/py/workplace/a720/t9 7-23-17-56/t9new2/t9new/t9/t8/project_name/static/js/assets/img/backgrounds/2.jpg'},
                                             //             {image : 'H:/py/workplace/a720/t9 7-23-17-56/t9new2/t9new/t9/t8/project_name/static/js/assets/img/backgrounds/3.jpg'},

                             //    {image : '/static/js/assets/img/backgrounds/3.jpg'}
                                 {image : '/static/js/assets/img/backgrounds/1.jpg'},
                                 {image : '/static/js/assets/img/backgrounds/2.jpg'},
                                 {image : '/static/js/assets/img/backgrounds/3.jpg'}
                             ]

    });

});
