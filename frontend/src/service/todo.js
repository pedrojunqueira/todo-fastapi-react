// Service for interacting with the backend Todo API
const API_URL = "http://localhost:8004";

export async function fetchTodos() {
  const response = await fetch(`${API_URL}/todos/`);
  if (!response.ok) throw new Error("Failed to fetch todos");
  return response.json();
}

export async function createTodo(text) {
  const response = await fetch(`${API_URL}/todos/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  if (!response.ok) throw new Error("Failed to create todo");
  return response.json();
}

export async function updateTodo(id, text, completed) {
  const response = await fetch(`${API_URL}/todos/${id}/`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, completed }),
  });
  if (!response.ok) throw new Error("Failed to update todo");
  return response.json();
}

export async function deleteTodo(id) {
  const response = await fetch(`${API_URL}/todos/${id}/`, {
    method: "DELETE",
  });
  if (!response.ok) throw new Error("Failed to delete todo");
  return response.json();
}
