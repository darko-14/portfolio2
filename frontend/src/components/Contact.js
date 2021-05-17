import React from 'react'

const Contact = () => {
    return (
        <div>
            <form>
                <label>Name</label><br/>
                <input type='text'/><br/>
                <label>Email</label><br/>
                <input type='email'/><br/>
                <labe>Message</labe><br/>
                <textarea rows='5'></textarea><br/>
                <button type='submit'>Submit</button>
            </form>
        </div>
    )
}

export default Contact
