import { useContext } from "react";
import { TodoContext } from "../context/TodoContext";

export function useTodo() {
  return useContext(TodoContext);
}
