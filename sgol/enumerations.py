SGOL_CLAUSES = [
    {
        "id": "ADD",
        "description": "ADD is used for adding elements to the graph.",
        "examples": [
            "... RELATE ADD"
        ],
        "input": "elements",
        "output": "void"
    },
    {
        "id": "DISCARD",
        "description": "DISCARD",
        "input": "any",
        "output": "void",
        "examples": [
            "SELECT $PointOfInterestType UPDATE poi_types DISCARD SELECT ..."
        ]
    },
    {
        "id": "FETCH",
        "description": "FETCH is used for replacing the primary set of elements with a secondary set.",
        "input": "any",
        "output": "elements"
    },
    {
        "id": "HAS",
        "description": "HAS is the operation for filtering the current set of entities to only those connected to another literal set of entities. It is frequently used within a chain of statements.",
        "input": "elements",
        "output": "elements",
        "examples": [
            "... HAS INPUT $HasType pointofinteresttype_cafe OUTPUT entities"
        ]
    },
    {
        "id": "INIT",
        "description": "INIT initializes a secondary set of objects, typically elements.",
        "input": "any",
        "output": "void",
        "examples": [
            "INIT poi_types"
        ]
    },
    {
        "id": "LIMIT",
        "description": "LIMIT is the operation for limiting the size of the current set of entities to the given value. It is frequently used as a penultimate operation after a search, after FETCH and before OUTPUT.",
        "input": "elements",
        "output": "elements",
        "examples": [
            "SELET $PointOfInterest LIMIT 10 OUTPUT entities"
        ]
    },
    {
        "id": "NAV",
        "description": "NAV is the operation for navigating / transversing / hopping around the graph from entity to entity following certain edges.",
        "input": [
            "elements", "void"
        ],
        "output": "elements",
        "examples": [
            "NAV $PointOfInterest $HASTYPE pointofinteresttype_cafe"
        ]
    },
    {
        "id": "OUTPUT",
        "description": (
            "Output is used to specify the type of objects returned by the"
            " chain of operations. This is used for encoding the response"
            " to SGOL clients. void can be used to signal that there is no"
            " response (like a SQL update). If the output type is missing"
            " or invalid for the chain, the SGOL server may throw an error."
        ),
        "input": "any",
        "output": "void"
    },
    {
        "id": "RELATE",
        "description": (
            "RELATE is used for calculating the geospatial relationship"
            " between two sets of entities, the first set being the primary"
            " set and the second being a secondary set referenced by id."
            " The total number of calculations is in O(mn) time, so your"
            " SGOL-server may cache results to increase performance."
        ),
        "input": "entities",
        "output": "entities"
    },
    {
        "id": "RUN",
        "description": (
            "RUN is used for directly executing graph operations known to"
            " the server. It is frequently used at the end of a stream"
            " for transforming the output."
        ),
        "input": "varies",
        "output": "varies"
    },
    {
        "id": "SELECT",
        "description": (
            "SELECT is a basic operation, analagous to a SQL"
            " SELECT. It simply filters all the elements in the graph"
            " by a group and optionaly other filters. You can select"
            " an entity by it's id or select all the entities in a"
            " list of groups. If selecting by group, then use a"
            " comma-separated list with each group prepended by a $."
            " You can optionally, also save the output to a secondary"
            " set by id."
        ),
        "input": "void",
        "output": "entities",
        "examples": [
            "SELECT $PointOfInterest",
            "SELECT pointofinteresttype_cafe"
        ]
    }
]

SGOL_FILTERS = [
    {
        "id": "collectioncontains",
        "description": "Does the collection contain the value?",
        "examples": [
            "collectioncontains(aliases, \"bank\")",
            "collectioncontains(keywords, medical)"
        ]
    },
    {
        "id": "bbox",
        "description": "Bounding box spatial filter",
        "examples": [
            "bbox(-50,-10,10,50)"
        ]
    },
    {
        "id": "dwithin",
        "description": "Is entity within the given distance from the given entity?",
        "examples": [
            "dwithin(geom_wkt, \"Logan Circle, DC\", 1000, meters)"
        ]
    }
]

SGOL_TYPES = [
    {
        "id": "void",
        "description": "The empty, none, etc. type."
    },
    {
        "id": "elements",
        "description": "A set of Graph elements"
    },
    {
        "id": "entities",
        "description": "A set of Graph entities"
    },
    {
        "id": "edges",
        "description": "A set of Graph edges"
    },
    {
        "id": "geometries",
        "description": "A set of geometries"
    },
    {
        "id": "geometry",
        "description": (
            "A singular geometry object.  Will typically be a geometry"
            " collection when merging multiple geometries."
        )
    }
]
