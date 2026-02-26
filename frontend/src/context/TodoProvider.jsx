import { useEffect, useState } from "react";
import { TodoContext } from "./TodoContext";
import {
  fetchTodos,
  createTodo,
  updateTodo,
  deleteTodo,
} from "../service/todo";

export function TodoProvider({ children }) {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadTodos();
  }, []);

  async function loadTodos() {
    setLoading(true);
    try {
      const data = await fetchTodos();
      setTodos(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function addTodo(text) {
    if (!text.trim()) return;
    try {
      const newTodo = await createTodo(text);
      setTodos((prev) => [...prev, newTodo]);
    } catch (err) {
      setError(err.message);
    }
  }

  async function toggleTodo(todo) {
    try {
      const updated = await updateTodo(todo.id, todo.text, !todo.completed);
      setTodos((prev) => prev.map((t) => (t.id === todo.id ? updated : t)));
    } catch (err) {
      setError(err.message);
    }
  }

  async function removeTodo(id) {
    try {
      await deleteTodo(id);
      setTodos((prev) => prev.filter((t) => t.id !== id));
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <TodoContext.Provider
      value={{ todos, loading, error, addTodo, toggleTodo, removeTodo }}
    >
      {children}
    </TodoContext.Provider>
  );
}
