import fetch from '../fetch.js'
export default{
    state:{
        data:[],
        show:true
    },
    mutations:{
        getMyDiaryData(state){
           var token=fetch.storage.get('token');
            $.ajax({
                type:"get",
                url:"http://39.108.217.186:80/book.php",
                dataType:"json",
                data:{
                  "token":token,
                  "op":"get",
                },
                success:(data)=>{
                  state.show=false;
                  var i=0;
                  while(data[i]){
                    var date = new Date(parseInt(data[i].beginTime)*1000);
                    var Y = date.getFullYear() + '-';
                    var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
                    var D = date.getDate() ;
                    data[i].beginTime=Y+M+D;
                    date = new Date(parseInt(data[i].endTime)*1000);
                    Y = date.getFullYear() + '-';
                    M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
                    D = date.getDate() ;
                    data[i].endTime=Y+M+D;
                    state.data.push(data[i])
                    i++;
                  }
                },
                error:function(e){
                  console.log(e.responseText)
                }
              })
        },
    }
}