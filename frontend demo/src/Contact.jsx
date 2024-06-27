import React, { useState } from 'react';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    message: '',
  });

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // alert(JSON.stringify(formData, null, 2));
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <label htmlFor="firstName" className="block text-gray-400">First name</label>
              <input
                id="firstName"
                name="firstName"
                type="text"
                placeholder="Enter your first name"
                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white border-gray-700"
                value={formData.firstName}
                onChange={handleChange}
              />
            </div>
            <div className="space-y-2">
              <label htmlFor="lastName" className="block text-gray-400">Last name</label>
              <input
                id="lastName"
                name="lastName"
                type="text"
                placeholder="Enter your last name"
                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white border-gray-700"
                value={formData.lastName}
                onChange={handleChange}
              />
            </div>
          </div>
          <div className="space-y-2">
            <label htmlFor="email" className="block text-gray-400">Email</label>
            <input
              id="email"
              name="email"
              type="email"
              placeholder="Enter your email"
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white border-gray-700"
              value={formData.email}
              onChange={handleChange}
            />
          </div>
          <div className="space-y-2">
            <label htmlFor="message" className="block text-gray-400">Message</label>
            <textarea
              id="message"
              name="message"
              placeholder="Enter your message"
              className="w-full px-3 py-2 border rounded-lg min-h-[100px] focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white border-gray-700"
              value={formData.message}
              onChange={handleChange}
            />
          </div>
          <button
            type="submit"
            className="px-4 py-2 font-semibold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
};

export default ContactForm;
