
var createAllErrors = function() {
    var form = $( this )
    var showAllErrorMessages = function() {
        $.each(form[0], function(index, value){
            if (this.labels!=null ){
                if (this.id!=""){
                    $('ul.errorMessages-'+this.id).html('');
                }
            }
        }) 
        // Find all invalid fields within the form.
        var invalidFields = form.find( ":invalid" ).each( function( index, node ) { 
                errorList = $("ul.errorMessages-"+node.id, form );
                errorList.empty();
                errorList.append(`<div class="field-error-text" id="error-div-${node.id}"></div>`)

            // Find the field's corresponding label
            var label = $( "#"+node.id),
                // Opera incorrectly does not fill the validationMessage property.
                message = node.validationMessage || 'Invalid value.';
                //console.log(label,node.id,message, label[0]['labels'][0]['innerText'])

            errorList
                .show()
                
                /*try {
                    $('#error-div-'+node.id).append( `<strong>
                        ${label[0]['labels'][0]['innerText']} </strong> : <span>  ${ message } </span><br>
                    `);
                }
                catch(err) {*/
                    $('#error-div-'+node.id).append( `
                         <span>  <i class="sop-error me-1"></i> ${ message } </span><br>
                    `);
               // }
        });
        
    };

    // Support Safari
    form.on( ".form-submit", function( event ) {
        if ( this.checkValidity && !this.checkValidity() ) {
            $( this ).find( ":invalid" ).first().focus();
            event.preventDefault();
        }
    });

    $( ".form-submit", form )
        .on( "click", showAllErrorMessages);
        
    $( ".form-next", form )
        .on( "click", showAllErrorMessages);
    

    $( "input", form ).on( "keypress", function( event ) {
        var type = $( this ).attr( "type" );
        if ( /date|email|month|number|search|tel|text|time|url|week/.test ( type )
            && event.keyCode == 13 ) {
            showAllErrorMessages();
        }
    });
};