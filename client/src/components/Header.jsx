import Logo from "../assets/Bixiflowgo.png";
import "./Header.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";

export default function Header() {
  return (
    <div className="bg-sky-200">
      <div className="flex justify-between items-center">
        <div className="flex items-center">
          <img
            onClick={(e) => {
              window.location = "/";
            }}
            src={Logo}
            className="size-24 hover:scale-110 transition"
          />
          <p className="font-mono text-2xl font-semibold">BixiFlow</p>
        </div>
        {window.location.href !== "/" && (
          <div className="flex gap-3 pr-24 search">
            <input
              className="border-2 border-sky-400 rounded-md h-7"
              type="search"
              placeholder="Search for a location!"
            />
            <button
              className="bg-green-300 rounded-md h-7 mr-10 size-9
          "
            >
              <FontAwesomeIcon icon={faSearch} />
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
