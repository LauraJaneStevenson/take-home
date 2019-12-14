
const completeTask = (id) => {

    $.post('/complete_task',{ 'id':id }, (res) => {

        
        alert(res);
    });

};

// $('#update').on('click', () => {

    $.get('/all_tasks.json',(res)=>{

        for(const task of res){

            if(task.complete){
                $('ul.tasks').append(
                    `<input class="form-check-input" 
                    type="checkbox" 
                    id="invalidCheck"
                    onclick="">
                    <li class="done" id="${task.id}">${task.task_str}</li>`
                    );
            }else{

                $('ul.tasks').append(
                    `<input class="form-check-input" 
                    type="checkbox"  
                    id="invalidCheck"
                    onclick="completeTask(${task.id})">
                    <li id="${task.id}">${task.task_str}</li>`
                    );
            }
        };
    });




// });