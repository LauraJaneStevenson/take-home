$.get('/all_tasks.json',(res)=>{

    for(const task of res){
        if(task.complete){
            $('ul.tasks').append(
                `<input class="form-check-input" type="checkbox" value="" id="invalidCheck">
                <li class='done'>${task.task_str}</li>`
                );
        }else{
            $('ul.tasks').append(
                `<input class="form-check-input" type="checkbox" value="" id="invalidCheck">
                <li>${task.task_str}</li>`
                );
        }
    }
});

// <div class="form-check">
//       <input class="form-check-input" type="checkbox" value="" id="invalidCheck">
//       <label class="form-check-label" for="invalidCheck">
//         Agree to terms and conditions
//       </label>
//       <div class="invalid-feedback">
//         You must agree before submitting.
//       </div>

