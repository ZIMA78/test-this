<html>
 <head>
 <title>Задачи на день</title>
 <link rel="stylesheet" href="static/styles.css">
 <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
 <script src="static/script.js"></script>
 </head>
 <body>
 <div class="container">
 <h1>Текущие задачи  {{total_tasks}}, {{incomplete}}</h1>
 <ul id="todo-list">
 % for task in tasks:
 % if task.is_completed:
 <li class="completed">
 <input class='checkbox' data-uid={{ task.uid }} type='checkbox'
disabled='disabled' checked='checked'/>
 % else:
 <li>
 <input class='checkbox' data-uid={{ task.uid }} type='checkbox' />
 % end
 {{ task }}
 <a class="remove" href="/api/delete/{{ task.uid }}">X</a>
 <hr/>
 </li>
 % end
 </ul>
<form id="todo-add" action="/add-task" method="post">
 <input class="form-control" type="text" name="description"/>
 <button class="add" type="submit">+</button>
 % for d in f:
 {{d}}
</form>
 </form>
 </div>
 </body>
</html>
