export default{
    state:{
        diaryData:[],
        show:true
    },
    mutations:{
        getIndexData(state){
           
            $.ajax({
                type:"post",
                url:"http://39.108.217.186:80/diary.php",
                dataType:"json",
                data:{
                    "op":"getIndex"
                },
                async:false,
                success:function(data){
                    var i=0;
                    state.show=false;
                    while(data[i]){
                        var date = new Date(parseInt(data[i].createTime)*1000);
                        var Y = date.getFullYear() + '-';
                        var h = date.getHours() + ':';
                        var m = date.getMinutes() + ':';
                        var s = date.getSeconds();
                        data[i].createTime=h+m+s;
                        state.diaryData.push(data[i])
                        i++;
                    }
                    state.diaryData.reverse()
                },
                error:function(e){
                    console.log(e.responseText)
                }
            })
        }
    }
}