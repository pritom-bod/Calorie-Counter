var table = document.getElementById("table");
    var carbs = 0, protine=0, fat=0, calories=0;

    for(var i=1; i<table.rows.length-1; i++){
        console.log(table.rows[i].cells[1].innerHTML);
        carbs +=parseFloat(table.rows[i].cells[1].innerHTML);
        carbs = Math.round(carbs);
        protine += parseFloat(table.rows[i].cells[2].innerHTML);
        protine = Math.round(protine);
        fat += parseFloat(table.rows[i].cells[3].innerHTML);
        fat = Math.round(fat)
        calories += parseFloat(table.rows[i].cells[4].innerHTML);
        calories = Math.round(calories)
    }
    
    
    document.getElementById("totalCarbs").innerHTML='<b>'+ carbs +'(g)</b>';

    document.getElementById("totalProtine").innerHTML='<b>'+ protine +'(g)</b>';
    
    document.getElementById("totalFats").innerHTML='<b>'+ fat +'(g)</b>';
    
    document.getElementById("totalCalories").innerHTML='<b>'+ calories +'(g)</b>';

    var calPer = (calories/2000) *100; 
    document.getElementsByClassName('progress-bar')[0].setAttribute("style","width:"+calPer+"%");



