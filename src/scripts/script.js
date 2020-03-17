function set_content_in_divs(paragraphs) {
    $.each(paragraphs, function(i, d) {
        console.log(paragraphs)
        p = $("#paragraph-" + i)
        if($("#paragraph-" + i).length == 0) {
            $("div#container").append("<div class='col-4' id='#paragraph-" + i + "'>" + d + "</div>");
        }else{
            p.html("<p>" + d + "</p>")
        }
    })
}

$("#date").click(function(){
    console.log("i am here: 1")
    $.getJSON("/api/forecasts", function(data){
        set_content_in_divs(data['prophecies'])
    })
})
