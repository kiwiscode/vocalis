import { useState } from "react";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Link } from "react-router-dom";
import useAxios from "../../hooks/useAxios";
import { API_URL } from "../../constants/env";

interface RegisterFormData {
  email: string;
  password: string;
}

const RegisterForm = () => {
  const { response, error, loading, fetchData } = useAxios();
  const [formData, setFormData] = useState<RegisterFormData>({
    email: "",
    password: "",
  });

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const data = await fetchData({
        url: `${API_URL}/register`,
        method: "POST",
        data: formData,
      });
      console.log("Register success:", data);
    } catch (err) {
      console.error("Register error:", err);
    }
  };

  return (
    <div className="register-form-wrapper max-w-[1290px] mx-auto flex flex-col justify-center items-center h-[100vh]">
      <div className="pb-[2rem]">
        <h1>Create an account</h1>
      </div>
      <form
        className="w-[340px] flex flex-col gap-[1.5rem]"
        onSubmit={handleSubmit}
      >
        <Input
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          className="rounded-[9999px] min-h-[52px]"
          placeholder="Email address"
          type="email"
        />
        <Input
          value={formData.password}
          onChange={(e) =>
            setFormData({ ...formData, password: e.target.value })
          }
          className="rounded-[9999px] min-h-[52px]"
          placeholder="Password"
          type="password"
        />
        <Button
          disabled={loading}
          className="rounded-[999px] bg-[#131313] hover:bg-[#333333] p-[1.5rem] cursor-pointer min-h-[52px] w-full font-normal text-sm"
          size={"lg"}
          type="submit"
        >
          {loading ? "Loading..." : "Continue"}
        </Button>
      </form>
      {error && <p className="text-red-500 mt-4">{error}</p>}
      <p className="text-center text-[16px] pt-[1.5rem]">
        Already have an account?{" "}
        <span className="hover:underline cursor-pointer">
          <Link to="/login" className="text-[#3e68ff]">
            Log in
          </Link>
        </span>
      </p>
    </div>
  );
};

export default RegisterForm;
