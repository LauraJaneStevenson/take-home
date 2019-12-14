$.get('/all_tasks.json',(res)=>{

    for(const task of res){
        if(task.complete){
            $('ul.tasks').append(
                `<li class='done'>${task.task_str}</li>`
                );
        }else{
            $('ul.tasks').append(
                `<li>${task.task_str}</li>`
                );
        }
    }
});

