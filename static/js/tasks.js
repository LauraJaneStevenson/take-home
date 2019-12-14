
const completeTask = (id) => {



    $.post('/complete_task',{ 'id':id }, (res) => {

        alert(res);
    });

};



$.get('/all_tasks.json',(res)=>{

    for(const task of res){

        if(task.complete){
            $('ul.tasks').append(
                `<input class="form-check-input" 
                type="checkbox" 
                id="invalidCheck"
                onclick="">
                <li class='done'>${task.task_str}</li>`
                );
        }else{

            $('ul.tasks').append(
                `<input class="form-check-input" 
                type="checkbox"  
                id="invalidCheck"
                onclick="completeTask(${task.id})">
                <li>${task.task_str}</li>`
                );
        }
    };
});



// $('li.form-check-input').on('click', () => {

//     alert('HEY!')

// });