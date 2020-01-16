
const completeTask = (id) => {

    $.post('/complete_task',{ 'id':id }, (res) => {

        location.reload(true);
        // alert(res);
    });

};


const deleteTask = (id) => {

    $.post('/delete_task',{ 'id':id }, (res) => {

        location.reload(true);
    });

};


$('#update').on('click', () => {

   
            location.reload(true);

 });

$.get('/all_tasks.json',(res)=>{

    for(const task of res){

        if(task.complete){
            $('ul.tasks').append(
                `<input class="form-check-input" 
                type="checkbox" 
                id="invalidCheck"
                onclick="completeTask(${task.id})"
                checked>
                <li class="done" id="${task.id}">${task.task_str}<i class="fas fa-trash-alt" onclick="deleteTask(${task.id})"></i></li>`
                );
        }else{

            $('ul.tasks').append(
                `<input class="form-check-input" 
                type="checkbox"  
                id="invalidCheck"
                onclick="completeTask(${task.id})">
                <li id="${task.id}">${task.task_str}<i class="fas fa-trash-alt" onclick="deleteTask(${task.id})"></i></li>`
                );
        }
    };
});



