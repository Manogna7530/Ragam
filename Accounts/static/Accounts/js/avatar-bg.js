 // // ==== Avatar Image ===== // // 
 $(".avatar-img").each(function() {
    var name= $(this).find('p').text();
    updateColor(name,'dark',this);   
})

function stringToHslColor(str, s, l) {
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }    
    var h = hash % 360;
    return 'hsl('+h+', '+s+'%, '+l+'%)';
    }
    function updateColor(name,shade,ele) {               
    //console.log(ele);
    var textColor = shade=="light" ? '#555' : '#fff';                                                                    
    var hexColor = (shade=="light") ? stringToHslColor(name, 75 , 83): stringToHslColor(name,55,65);
    $(ele).css('background-color', hexColor);
    $(ele).css('color', textColor);
    }
    const page = "{{pagename}}";
    if (page == 'home') {
    $('.header-nav').addClass('d-none');
    }
    function stringHasTheWhiteSpaceOrNot(value){
    return value.indexOf(' ') >= 0;
}