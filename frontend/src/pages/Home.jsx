import { useEffect, useState } from "react";

import ExhibitCard from "../components/ExhibitCard";
import { getExhibits } from "../api/exhibits";


function Home() {
  const [exhibits, setExhibits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


  useEffect(() => {
    async function loadExhibits() {
      try {
        const data = await getExhibits();
        setExhibits(data);
      } catch (err) {
        setError("Unable to load exhibits.");
      } finally {
        setLoading(false);
      }
    }

    loadExhibits();
  }, []);


  if (loading) {
    return <p>Loading exhibits...</p>;
  }


  if (error) {
    return <p>{error}</p>;
  }


  return (
    <main>
      <h1>Houston Zoo</h1>

      <p>Explore our exhibits.</p>

      <div className="card-grid">
        {exhibits.map((exhibit) => (
          <ExhibitCard
            key={exhibit.id}
            exhibit={exhibit}
          />
        ))}
      </div>

      {/* Students will add the Animals section here */}
    </main>
  );
}


export default Home;