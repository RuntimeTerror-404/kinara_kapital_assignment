import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./StudentData.css";

const StudentData = () => {
    const [students, setStudents] = useState([]);
    const [page, setPage] = useState(1);
    const [pageSize, setPageSize] = useState(10);
    const [totalPages, setTotalPages] = useState(1);
    const [filters, setFilters] = useState({ name: '', total_marks: '' });

    useEffect(() => {
        fetchStudents();
    }, [page, filters]);

    const fetchStudents = async () => {
        const response = await axios.get(`http://127.0.0.1:5000/students`, {
            params: {
                page: page,
                page_size: pageSize,
                name: filters.name,
                total_marks: filters.total_marks
            }
        });
        setStudents(response.data.students);
        setTotalPages(response.data.pages);
    };

    const handleFilterChange = (e) => {
        setFilters({ ...filters, [e.target.name]: e.target.value });
        setPage(1); // Reset to page 1 when filters change
    };

    return (
      <div className="container">
        <h1>Kinara Capital SDE Home assignment</h1>
        <h4>By Mohit Parashar</h4>
  
        <div className="filters">
          <label>Name Filter: </label>
          <input
            type="text"
            name="name"
            value={filters.name}
            onChange={handleFilterChange}
          />
          <label>Marks Filter: </label>
          <input
            type="number"
            name="total_marks"
            value={filters.total_marks}
            onChange={handleFilterChange}
          />
        </div>
  
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Total Marks</th>
            </tr>
          </thead>
          <tbody>
            {students.map(student => (
              <tr key={student.id}>
                <td>{student.id}</td>
                <td>{student.name}</td>
                <td>{student.total_marks}</td>
              </tr>
            ))}
          </tbody>
        </table>
  
        <div className="pagination">
          <button disabled={page === 1} onClick={() => setPage(page - 1)}>Previous</button>
          <button disabled={page === totalPages} onClick={() => setPage(page + 1)}>Next</button>
        </div>
      </div>
    );
};

export default StudentData;
