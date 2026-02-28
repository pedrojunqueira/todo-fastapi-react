import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import {
  fetchTodos,
  createTodo,
  updateTodo,
  deleteTodo,
} from "../service/todo";

export function useTodo() {
  const queryClient = useQueryClient();

  const { data: todos = [], isLoading: loading, error } = useQuery({
    queryKey: ["todos"],
    queryFn: fetchTodos,
  });

  const addMutation = useMutation({
    mutationFn: (text) => createTodo(text),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
  });

  const toggleMutation = useMutation({
    mutationFn: (todo) => updateTodo(todo.id, todo.text, !todo.completed),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
  });

  const removeMutation = useMutation({
    mutationFn: (id) => deleteTodo(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
  });

  return {
    todos,
    loading,
    error: error?.message ?? null,
    addTodo: (text) => addMutation.mutate(text),
    toggleTodo: (todo) => toggleMutation.mutate(todo),
    removeTodo: (id) => removeMutation.mutate(id),
  };
}
