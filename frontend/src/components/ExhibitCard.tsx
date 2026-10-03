import type { Exhibit } from "../types/exhibit";

interface ExhibitCardProps {
  exhibit: Exhibit;
}

function ExhibitCard({ exhibit }: ExhibitCardProps) {
  return (
    <div>
      <h2>{exhibit.name}</h2>
      <p>{exhibit.location}</p>
      <p>{exhibit.description}</p>
    </div>
  );
}

export default ExhibitCard;