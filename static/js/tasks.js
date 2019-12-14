$.get('/all_tasks.json',(res)=>{

    for(const task of res){

        $('ul.tasks').append(
            `<li>${task.task_str}</li>`
            );
    }
});

