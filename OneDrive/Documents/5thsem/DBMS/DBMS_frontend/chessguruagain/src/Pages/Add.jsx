// Frontend AddGameForm.js

import React, { useState } from 'react';
import axios from 'axios';

const AddGameForm = () => {
  const [formData, setFormData] = useState({
    match_id: '',
    player1: '',
    player2: '',
    avg_fide_rating: '',
    tournament: '',
    year: '',
    link: '',
    opening_name: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post('http://localhost:8800/prevgames', formData);
      console.log('Game added successfully!');
    } catch (error) {
      console.error('Error adding game:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Match ID:</label>
      <input type="text" name="match_id" value={formData.match_id} onChange={handleChange} />

      <label>Player 1:</label>
      <input type="text" name="player1" value={formData.player1} onChange={handleChange} />

      <label>Player 2:</label>
      <input type="text" name="player2" value={formData.player2} onChange={handleChange} />

      <label>Avg FIDE Rating:</label>
      <input type="text" name="avg_fide_rating" value={formData.avg_fide_rating} onChange={handleChange} />

      <label>Tournament:</label>
      <input type="text" name="tournament" value={formData.tournament} onChange={handleChange} />

      <label>Year:</label>
      <input type="text" name="year" value={formData.year} onChange={handleChange} />

      <label>Link:</label>
      <input type="text" name="link" value={formData.link} onChange={handleChange} />

      <label>Opening Name:</label>
      <input type="text" name="opening_name" value={formData.opening_name} onChange={handleChange} />

      <button type="submit">Add</button>
    </form>
  );
};

export default AddGameForm;
