create table nodes (
	node_id SERIAL PRIMARY KEY,
	parent INTEGER REFERENCES nodes(node_id) ON DELETE CASCADE,
	title text,
	description text,
	status text DEFAULT 'expired',
    excluded text DEFAULT 'false',
	time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table reports (
	id SERIAL PRIMARY KEY,
	report_id text NOT NULL,
	parent INTEGER REFERENCES nodes(node_id) ON DELETE CASCADE,
	title text NOT NULL,
	description text NOT NULL,
	value NUMERIC,
	excluded text DEFAULT 'false',
	time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rules (  
    rule_id SERIAL PRIMARY KEY,
    parent_node_id INTEGER REFERENCES nodes(node_id) ON DELETE CASCADE,
    operator text NOT NULL,
    conditions JSONB NOT NULL,  
    action text NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 