import {
  fetchTodos,
  createTodo,
  updateTodo,
  deleteTodo,
} from "./service/todo.js";

async function testTodoService() {
  try {
    // Create a new todo
    const newTodo = await createTodo("Test from service");
    console.log("Created Todo:", newTodo);

    // Fetch all todos
    const todos = await fetchTodos();
    console.log("Fetched Todos:", todos);

    // Update the created todo
    const updated = await updateTodo(newTodo.id, "Updated from service", true);
    console.log("Updated Todo:", updated);

    // Delete the created todo
    const deleted = await deleteTodo(newTodo.id);
    console.log("Deleted Todo:", deleted);
  } catch (error) {
    console.error("Service test error:", error);
  }
}

testTodoService();
