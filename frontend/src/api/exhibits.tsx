import type { Exhibit } from "../types/exhibit";

const API_URL = "http://localhost:8000";

export async function getExhibits(): Promise<Exhibit[]> {
  const response = await fetch(`${API_URL}/exhibits/`);

  if (!response.ok) {
    throw new Error("Failed to fetch exhibits");
  }

  return response.json();
}