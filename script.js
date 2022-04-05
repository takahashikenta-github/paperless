$(function(){
    /*=======================================================*/
    /*==========index.htmlの'サインイン'のhover色変換==========*/
    /*=======================================================*/
    $('.form-button input').hover(
        function(){
            $('.form-button input').css("background-color","#4682b4");},
        function(){
            $('.form-button input').css("background-color","#005e7a");
        }
    );

    /*=================================================*/
    /*==========home.htmlの各項目のhover色変更==========*/
    /*=================================================*/
    $('.select-button input').hover(
        function(){
            $(this).css("color","#a9a9a9");},
        function(){
            $(this).css("color","#252525");
        }
    );
    $('.select-button input').hover(
        function(){
            $(this).css("border-bottom-color","#a9a9a9");},
        function(){
            $(this).css("border-bottom-color","#252525");
        }
    );

    /*==================================================*/
    /*==========diary.htmlの各項目のhover色変更==========*/
    /*==================================================*/
    $('#button').click(
        function(){
            $(this).hide();
        }
    );

});