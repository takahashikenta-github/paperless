$(function(){

    let week_list = ['月', '火', '水', '木', '金'];
    //var dt_now = new Date();
    //var week = week_list[dt_now.getDay()-1];
    var week = week_list[3-1];
    let lessons = [
                    ['サーバー構築','奥田先生','サーバー構築','奥田先生','キャリアガイダンス','北畑先生'],
                    ['ゼミナールⅢ','島田先生','テクニカルⅡ','荒井先生','テクニカルⅢ','鳥居先生'],
                    ['ゼミナールⅢ','島田先生','データベースⅢ','佐々木先生','テクニカルⅡ','鳥居先生'],
                    ['ゼミナールⅢ','島田先生','テクニカルⅡ','鳥居先生','　','　'],
                    ['情報セキュリティーⅡ','薮木先生','Ｗｅｂアプリケーション','山本先生','Ｗｅｂアプリケーション','山本先生']
                ];

    $('#subject1').html(lessons[week_list.indexOf(week)][0]);
    $('#teacher1').html(lessons[week_list.indexOf(week)][1]);
    $('#subject2').html(lessons[week_list.indexOf(week)][2]);
    $('#teacher2').html(lessons[week_list.indexOf(week)][3]);
    $('#subject3').html(lessons[week_list.indexOf(week)][4]);
    $('#teacher3').html(lessons[week_list.indexOf(week)][5]);

});