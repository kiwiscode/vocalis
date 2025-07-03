import axios from "axios";

function App() {
  console.log(import.meta.env.VITE_API_URL);
  const getResponse = async () => {
    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/healthy`);

      console.log("res:", res);
    } catch (error) {}
  };
  return (
    <>
      <button onClick={getResponse}>
        Receive response from python+flask backend
      </button>
    </>
  );
}

export default App;
